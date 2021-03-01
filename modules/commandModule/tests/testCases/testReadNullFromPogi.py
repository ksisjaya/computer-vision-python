import json
import logging
import unittest
from ...commandModule import CommandModule

class TestReadingNullFromPOGIFiles(unittest.TestCase):

    def setUp(self):
        self.logger = logging.basicConfig(level=logging.DEBUG, )
        self.pogiData = dict()
        self.pogiFile = str(__file__).replace("\\testCases\\testReadNullFromPogi.py", "\\testJSONs\\test.json")
        self.commandModule = CommandModule(pogiFileDirectory=self.pogiFile)

    def tearDown(self):
        self.pogiData = dict()

        """
        
        return no error code if null
        
        
        return no 
        
        
        
        """
    def __value_instantiate(self, key, value):
        with open(self.pogiFile, "w") as file:
            dict = {key: value}
            json.dump(dict, file, ensure_ascii=False, indent=4, sort_keys=True)

    def test_error_code_if_equals_null(self):
        with self.assertRaises(SystemExit) as cm:
            self.commandModule.set_gps_coordinates(None)
        self.assertEqual(cm.exception.code, 1)

    def test_altitude_if_equals_none(self):
        self.__value_instantiate("altitude", None)
        with self.assertRaises(ValueError):
            self.commandModule.get_current_altitude()
    def test_airspeed_if_equals_none(self):
        self.__value_instantiate("airspeed", None)
        with self.assertRaises(ValueError):
            self.commandModule.get_current_airspeed()

    def test_is_landed_if_equals_none(self):
        self.__value_instantiate("is_landed", None)
        with self.assertRaises(ValueError):
            self.commandModule.get_is_landed()

    def test_euler_camera_if_equals_none(self):
        self.__value_instantiate("euler_camera", None)
        with self.assertRaises(ValueError):
            self.commandModule.get_euler_camera()

    def test_euler_camera_alpha_if_equals_none(self):
        euler_camera = {"alpha": None, "beta": 0.0, "gamma": 0.0}
        self.__value_instantiate("euler_camera", euler_camera)
        with self.assertRaises(ValueError):
            self.commandModule.get_euler_camera()

    def test_euler_camera_beta_if_equals_none(self):
        euler_camera = {"alpha": 0.0, "beta": None, "gamma": 0.0}
        self.__value_instantiate("euler_camera", euler_camera)
        with self.assertRaises(ValueError):
            self.commandModule.get_euler_camera()

    def test_euler_camera_gamma_if_equals_none(self):
        euler_camera = {"alpha": 0.0, "beta": 0.0, "gamma": None}
        self.__value_instantiate("euler_camera", euler_camera)
        with self.assertRaises(ValueError):
            self.commandModule.get_euler_camera()

    def test_euler_plane_if_equals_none(self):
        self.__value_instantiate("euler_plane", None)
        with self.assertRaises(ValueError):
            self.commandModule.get_euler_plane()

    def test_euler_plane_alpha_if_equals_none(self):
        euler_camera = {"alpha": None, "beta": 0.0, "gamma": 0.0}
        self.__value_instantiate("euler_camera", euler_camera)
        with self.assertRaises(ValueError):
            self.commandModule.get_euler_camera()


    def test_euler_plane_beta_if_equals_none(self):
        euler_camera = {"alpha": 0.0, "beta": None, "gamma": 0.0}
        self.__value_instantiate("euler_camera", euler_camera)
        with self.assertRaises(ValueError):
            self.commandModule.get_euler_camera()

    def test_euler_plane_gamma_if_equals_none(self):
        euler_plane= {"alpha": 0.0, "beta": 0.0, "gamma": None}
        self.__value_instantiate("euler_plane", euler_plane)
        with self.assertRaises(ValueError):
            self.commandModule.get_euler_plane()

    def test_gps_if_equals_none(self):
        self.__value_instantiate("gps", None)
        with self.assertRaises(ValueError):
            self.commandModule.get_gps_coordinate()

    def test_gps_lat_if_equals_none(self):
        gps = {"lat": None, "lng": 0.0}
        self.__value_instantiate("gps", gps)
        with self.assertRaises(ValueError):
            self.commandModule.get_gps_coordinate()

    def test_gps_lng_if_equals_none(self):
        gps = {"lat": 0.0, "lng": None}
        self.__value_instantiate("gps", gps)
        with self.assertRaises(ValueError):
            self.commandModule.get_gps_coordinate()
