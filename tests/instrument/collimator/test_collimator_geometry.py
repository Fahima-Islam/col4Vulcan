from col4Vulcan.instrument.collimator.collimator_zigzagBlade_old import Collimator_geom
import os
from instrument.geometry.pml import weave
from instrument.geometry import  operations,shapes
from instrument.geometry.pml.Renderer import Renderer as base
import pytest
parent_dir = os.path.abspath(os.pardir)
sample_path = os.path.join (parent_dir, 'sample')

coll_geo_file_name= 'coll_geometry.xml'
coll_geo_file = os.path.join(sample_path, coll_geo_file_name)

# class File_inc_Renderer(base):
#     def _renderDocument(self, body):
#         self.onGeometry(body)
#         return
#     def header(self):
#         return []
#     def footer(self):
#         return []
#     def end(self):
#         return

def test_create (coll_front_end_from_center,max_coll_len=60., Snap_angle=False, vertical_number_channels=20, horizontal_number_channels=20,
            detector_angles=[-45,-135],multiple_collimator=False, collimator_Nosupport=True, scad_flag=False,
            outputfile=coll_geo_file):

    length_of_each_part = max_coll_len
    coll_last_height_detector=150.
    coll_last_width_detector=60*2.
    min_channel_wall_thickness =1

    coll_last_front_end_from_center=coll_front_end_from_center+(2.*length_of_each_part)

    coll_last_back_end_from_center =coll_last_front_end_from_center+length_of_each_part

    coll_first=Collimator_geom()

    coll_first_inner_radius = coll_front_end_from_center + (0. * length_of_each_part)
    coll_first_outer_radius = coll_first_inner_radius + length_of_each_part

    coll_first_height_detector = (coll_last_height_detector / coll_last_back_end_from_center) * coll_first_outer_radius

    coll_first_width_detector = (coll_last_width_detector / coll_last_back_end_from_center) * coll_first_outer_radius  # half part


    coll_first.set_constraints(max_coll_height_detector=coll_first_height_detector,
                          max_coll_width_detector=coll_first_width_detector,
                          min_channel_wall_thickness=min_channel_wall_thickness,
                          max_coll_length=length_of_each_part,
                          min_channel_size=3,
                          collimator_front_end_from_center=coll_first_inner_radius,
                          collimator_parts=False,
                          no_right_border=False,
                          no_top_border=False,
                          horizontal_odd_blades=False,
                          vertical_odd_blades=False,
                          )

    fist_vertical_number_blades = 3
    fist_horizontal_number_blades = 3

    coll_first.set_parameters(vertical_number_channels=fist_vertical_number_blades,
                         horizontal_number_channels=fist_horizontal_number_blades,
                         channel_length=length_of_each_part)


    coll_middle = Collimator_geom()

    coll_middle_inner_radius = coll_front_end_from_center + (1. * length_of_each_part)

    coll_middle_outer_radius = length_of_each_part + coll_middle_inner_radius


    coll_middle_height_detector = (coll_last_height_detector / coll_last_back_end_from_center) * coll_middle_outer_radius

    coll_middle_width_detector = (coll_last_width_detector / coll_last_back_end_from_center) * coll_middle_outer_radius

    coll_middle.set_constraints(max_coll_height_detector=coll_middle_height_detector,
                          max_coll_width_detector=coll_middle_width_detector,
                          min_channel_wall_thickness=min_channel_wall_thickness,
                          max_coll_length=length_of_each_part,
                          min_channel_size=3,
                          collimator_front_end_from_center=coll_middle_inner_radius,
                          collimator_parts=True,
                          initial_collimator_horizontal_channel_angle=0.0,
                          initial_collimator_vertical_channel_angle=0.0,
                          remove_vertical_blades_manually=True,
                          vertical_blade_index_list_toRemove=[2, 5],
                          remove_horizontal_blades_manually=True,
                          horizontal_blade_index_list_toRemove=[2, 5],
                          no_right_border=False,
                          no_top_border=False,
                          vertical_even_blades=False,
                          horizontal_even_blades=False)

    coll_middle.set_parameters(vertical_number_channels=(fist_vertical_number_blades) * 3,
                         horizontal_number_channels=(fist_horizontal_number_blades) * 3,
                         channel_length=length_of_each_part)

    col_last = Collimator_geom()

    col_last.set_constraints(max_coll_height_detector=coll_last_height_detector,
                                  max_coll_width_detector=coll_last_width_detector,
                                  min_channel_wall_thickness=min_channel_wall_thickness,
                                  max_coll_length=length_of_each_part,
                                  min_channel_size=3.,
                                  collimator_front_end_from_center=coll_last_front_end_from_center,
                                  remove_horizontal_blades_manually=True,
                                  horizontal_blade_index_list_toRemove=[2, 5, 11, 14, 20, 23],
                                  remove_vertical_blades_manually=True,
                                  vertical_blade_index_list_toRemove=[2, 5, 11, 14, 20, 23],
                                  collimator_parts=True,
                                  no_right_border=False,
                                  no_top_border=False,
                                  vertical_odd_blades=False,
                                  horizontal_odd_blades=False)


    col_last.set_parameters(vertical_number_channels=fist_vertical_number_blades * 9,
                                 horizontal_number_channels=fist_horizontal_number_blades * 9,
                                 channel_length=length_of_each_part)

    coliFirst = coll_first.gen_collimators(detector_angles=detector_angles, multiple_collimator=False,
                                             collimator_Nosupport=True)
    coliMiddle = coll_middle.gen_collimators(detector_angles=detector_angles, multiple_collimator=False,
                                        collimator_Nosupport=True)
    colilast =col_last.gen_collimators(detector_angles=detector_angles, multiple_collimator=False,collimator_Nosupport=True)


    whole = operations.unite(operations.unite(coliFirst, coliMiddle),colilast)

    # with open (outputfile,'wt') as file_h:
    #     weave(whole,file_h, print_docs = False,renderer=File_inc_Renderer(), author='')


# gen_col__xml(angular_spacing=2, channel_size=1, outsideCurveLength_fromSOurce=50, insideCurveLength_fromSOurce=0, coll_file=outputfile)
