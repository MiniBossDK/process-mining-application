import unittest
from unittest.mock import MagicMock, patch
import os
import tempfile
import pm4py
from pm4py.visualization.dcr import visualizer as dcr_visualizer
from app.controller import load_dcr_controller
from app.controller.load_dcr_controller import *



class TestSaveGvizAsSvg(unittest.TestCase):
    def test_save_gviz_as_svg_without_extension(self):
        # Create a mock gviz object
        gviz = MagicMock()
        output_path = 'test_output'

        with tempfile.TemporaryDirectory() as temp_dir:
            full_output_path = os.path.join(temp_dir, output_path)

            # Ensure the intermediate file does not exist
            if os.path.exists(full_output_path):
                os.remove(full_output_path)

            # Call the function
            save_gviz_as_svg(gviz, full_output_path)

            # Check that gviz.render was called with correct parameters
            gviz.render.assert_called_with(full_output_path, format='svg')

            # Check that the intermediate file was deleted if it existed
            self.assertFalse(os.path.exists(full_output_path))

    def test_save_gviz_as_svg_with_extension(self):
        # Create a mock gviz object
        gviz = MagicMock()
        output_path = 'test_output.svg'

        with tempfile.TemporaryDirectory() as temp_dir:
            full_output_path = os.path.join(temp_dir, output_path)

            intermediate_file = full_output_path[:-4]

            # Ensure the intermediate file does not exist
            if os.path.exists(intermediate_file):
                os.remove(intermediate_file)

            # Call the function
            save_gviz_as_svg(gviz, full_output_path)

            # Check that gviz.render was called with correct parameters
            gviz.render.assert_called_with(intermediate_file, format='svg')

            # Check that the intermediate file was deleted if it existed
            self.assertFalse(os.path.exists(intermediate_file))

    def test_save_gviz_as_svg_with_existing_intermediate_file(self):
        # Create a mock gviz object
        gviz = MagicMock()
        output_path = 'test_output'

        with tempfile.TemporaryDirectory() as temp_dir:
            full_output_path = os.path.join(temp_dir, output_path)

            # Create a dummy intermediate file
            with open(full_output_path, 'w') as f:
                f.write('dummy content')

            # Ensure the intermediate file exists
            self.assertTrue(os.path.exists(full_output_path))

            # Call the function
            save_gviz_as_svg(gviz, full_output_path)

            # Check that gviz.render was called with correct parameters
            gviz.render.assert_called_with(full_output_path, format='svg')

            # Check that the intermediate file was deleted
            self.assertFalse(os.path.exists(full_output_path))

class TestHandleLoad(unittest.TestCase):
    @patch('app.controller.load_dcr_controller.save_gviz_as_svg')
    @patch('pm4py.visualization.dcr.visualizer.apply')
    @patch('pm4py.discover_dcr')
    @patch('pm4py.read_xes')
    def test_handle_load(self, mock_read_xes, mock_discover_dcr, mock_visualizer_apply, mock_save_gviz_as_svg):
        # Set up the mocks
        mock_read_xes.return_value = 'event_log'
        mock_discover_dcr.return_value = ('graph', None)
        mock_visualizer_apply.return_value = 'gviz'

        path = 'pm4py_dcr.tests.input_data.roadtraffic100traces.xes'

        # Call the function
        handle_load(path)

        # Check that pm4py.read_xes was called with correct parameters
        mock_read_xes.assert_called_with(path)

        # Check that pm4py.discover_dcr was called with the event_log
        mock_discover_dcr.assert_called_with('event_log')

        # Check that dcr_visualizer.apply was called with the graph
        mock_visualizer_apply.assert_called_with('graph')

        # Check that save_gviz_as_svg was called with gviz and 'output.svg'
        mock_save_gviz_as_svg.assert_called_with('gviz', 'output.svg')
if __name__ == '__main__':
    unittest.main()
