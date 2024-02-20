import argparse
import numpy as np
import nibabel as nib
import os 

def main(args):
    path = os.path.join(args.path_output)
    os.mkdir(path)

    print("Registration saved in : ", args.path_output)
    # Crop IMAGE and WM mask with 10 pixels dilation of WM mask
    comand_1 = f"sct_crop_image -i {args.path_image} -m {args.mask_wm}  -dilate 10x10x0 -o {args.path_output}/image_crop.nii.gz"
    os.system(comand_1)
    comand_2 = f"sct_crop_image -i {args.mask_wm} -m {args.mask_wm}  -dilate 10x10x0 -o {args.path_output}/image_wm_crop.nii.gz"
    os.system(comand_2)
    # Registration of AMU7T template to subject space
    comand_3 = f"sct_register_to_template -i {args.path_output}/image_crop.nii.gz -s {args.path_output}/image_wm_crop.nii.gz -l {args.landmarks} -c t1 -v 1 -s-template-id 4  -t {args.path_template_AMU7T}  -param step=1,type=imseg,algo=centermassrot,rot_method=pcahog:step=2,type=seg,algo=bsplinesyn,slicewise=0,metric=MeanSquares,samplStrategy=None,samplPercent=0.2,iter=2,smooth=1,rot_method=pcahog:step=3,type=seg,algo=syn,metric=MeanSquares,shrink=2,dof=Tz_Rz_Sz,slicewise=1,iter=20 -ref subject -ofolder {args.path_output}"
    os.system(comand_3)
    # Registration of AMU7T atlas to subject space
    comand_4 = f"sct_apply_transfo -i {args.path_template_AMU7T}/atlas/AMU7T_50_labels.nii.gz -d {args.path_output}/image_crop.nii.gz  -w {args.path_output}/warp_template2anat.nii.gz -o {args.path_output}/labels_AMU7T2anat.nii.gz -x nn"
    os.system(comand_4)
    comand_5 = f"sct_warp_template -d {args.path_output}/image_crop.nii.gz -w {args.path_output}/warp_template2anat.nii.gz  -t {args.path_template_AMU7T} -ofolder {args.path_output}"
    os.system(comand_5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    	description= 
    	'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n'
    	'\n'
    	'Script for registrater AMU7T template to subject space. \n'
    	'This script applies SCT command lines: sct_crop_image, sct_register_to_template, sct_apply_transfo and sct_warp_template. \n'
    	'\n'
    	'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n',
        formatter_class=argparse.RawTextHelpFormatter )
        
    parser.add_argument("--path_image", required=True, help="Path to image (.nii.gz)")
    parser.add_argument("--mask_wm", required=True, help="Path to wm mask of (.nii.gz)")  
    parser.add_argument("--landmarks", required=True, help="Path to landmarks - C2 and C5 are recommended (.nii.gz)")
    parser.add_argument("--path_template_AMU7T", required=True, help="Path to AMU7T template")
    parser.add_argument("--path_output", required=True, help="Path output folder")
    args = parser.parse_args()
    main(args)    
