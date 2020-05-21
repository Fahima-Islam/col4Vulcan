from collimator_zigzagBlade_old import Collimator_geom, Parameter_error
import os, sys
parent_dir = os.path.abspath(os.pardir)
libpath = os.path.join(parent_dir, 'c3dp_source')
sample_path = os.path.join (parent_dir, 'sample')

coll_geo_file_name= 'coll_geometry_vulcan'
coll_geo_file = os.path.join(sample_path, coll_geo_file_name)
# detector_width= 203.41 , detector_height= 362
def create (detector_width= 350 , detector_height = 760,coll_front_end_from_center=444.5,length_coll=2000,
            chanel_length=501.9 , Snap_angle=False, vertical_number_channels=5,
            horizontal_number_channels=26,
            detector_angles=[150],multiple_collimator=False, collimator_Nosupport=True, scad_flag=False,
            outputfile=coll_geo_file):
    coll = Collimator_geom()
    detector_dist_fr_sample_center =coll_front_end_from_center+length_coll
    coll.set_constraints(max_coll_height_detector=detector_height,
                          max_coll_width_detector=detector_width,
                          min_channel_wall_thickness=2,
                          max_coll_length=length_coll,
                          min_channel_size=2.87,
                          wall_thickness=2,
                          collimator_front_end_from_center=coll_front_end_from_center,
                          detector_dist_fr_sample_center=detector_dist_fr_sample_center,
                          detector_size=detector_width,

                          )

    coll.set_parameters(vertical_number_channels=vertical_number_channels,
                        horizontal_number_channels=horizontal_number_channels,
                         channel_length=chanel_length)

    coll.gen_collimators_xml( detector_angles=detector_angles,multiple_collimator=multiple_collimator,
                              collimator_Nosupport=collimator_Nosupport,
                              scad_flag=scad_flag, coll_file=outputfile)




# gen_col__xml(angular_spacing=2, channel_size=1, outsideCurveLength_fromSOurce=50, insideCurveLength_fromSOurce=0, coll_file=outputfile)
