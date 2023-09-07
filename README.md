# AMU7T: 3D qT1 and T2*w in vivo template + atlas
AMU7T : high-resolution multimodal quantitative T1 and T2*-weighted templates with white and gray matter spinal cord and substructures atlas, aligned with the PAM50 space
![AMU_7T_template](https://github.com/spinalcordtoolbox/template_AMU7T/assets/77469192/3b5cb4b8-5931-4841-b952-d968f4b4338f)

## Data
This data repository contains:
- `template/AMU26_qt1.nii.gz`: 7T qT1 template from 26 subjects.
- `template/AMU72_t2s.nii.gz`: 7T T2*w template from 72 subjects.
- `template/AMU7T_gm.nii.gz`: Probabilistic gray matter mask.
- `template/AMU7T_wm.nii.gz`: Probabilistic white matter mask.
- `template/AMU7T_sc.nii.gz`: Probabilistic spinal cord mask.
- `atlas/AMU7T_50_labels.nii.gz`: Atlas with 50 labels (WM parcels from [Lévy et al., NeuroImage (2015)](https://pubmed.ncbi.nlm.nih.gov/26099457/)., and GM parcels derivated from _Hausman, _L. Atlases of the Spinal Cord and Brainstem and the Forebrain. (Thomas, 1962).__
- `atlas/AMU7T_label_ID_bin.nii.gz`: Binary masks by ID.

## Labels:  Multilabel atlas in in `atlas/AMU7T_50_labels.nii.gz` containing:

## **ID  -  Region**
- 0	  -  WM Left_fasciculus-gracilis		 
- 1	  -  WM Right_fasciculus-gracilis	   
- 2	  -  WM Left_fasciculus-cuneatus		
- 3	  -  WM Right_fasciculus-cuneatus	 	
- 4	  -  WM Left_lateral-corticospinal	
- 5	  -  WM Right_lateral-corticospinal	
- 6	  -  WM Left_ventral-spinocerebellar	
- 7	  -  WM Right_ventral-spinocerebellar
- 8	  -  WM Left_rubrospinal	 			      
- 9	  -  WM Right_rubrospinal	 		      
- 10 -	WM Left_lateral-reticulospinal	 	
- 11 -	WM Right_lateral-reticulospinal	 	      
- 12 -	WM Left_spinal-lemniscus-spinothalamic	
- 13 -	WM Right_spinal-lemniscus-spinothalamic	
- 14 -	WM Left_spino-olivary	 	            	
- 15 -	WM Right_spino-olivary	            	
- 16 -	WM Left_ventrolateral-reticulospinal  
- 17 -	WM Right_ventrolateral-reticulospinal	
- 18 -	WM Left_lateral-vestibulospinal	     	
- 19 -	WM Right_lateral-vestibulospinal	    
- 20 -	WM Left_ventral-reticulospinal	 		  
- 21 -	WM Right_ventral-reticulospinal	 	    
- 22 -	WM Left_ventral-corticospinal	 		    
- 23 -	WM Right_ventral-corticospinal	 		  
- 24 -	WM Left_tectospinal	 			            
- 25 -	WM Right_tectospinal	 			        
- 26 -	WM Left_medial-reticulospinal	 	    
- 27 -	WM Right_medial-reticulospinal	 	  
- 28 -	WM Left_medial-longitudinal-fasciculus	
- 29 -	WM Right_medial-longitudinal-fasciculus    
- 30 -	anterior-fissure	 			            
- 31 -	septum	 					                
- 32 -	GM Left_medial-ventral-horn	 		  
- 33 -	GM Left_central-ventral-horn    	
- 34 -	GM Left_lateral-ventral-horn	    
- 35 -	GM Right_medial-ventral-horn	 	  
- 36 -	GM Right_central-ventral-horn	 		
- 37 -	GM Right_lateral-ventral-horn	    
- 38 -	GM Left_dorsal-intermediate-zone	
- 39 -	GM Left_ventral-intermediate-zone	
- 40 -	GM Right_dorsal-intermediate-zone	
- 41 -	GM Right_ventral-intermediate-zone
- 42 -	GM Left_reticular-formation	 		  
- 43 -	GM Left_dorsomarginal-nucleus	 	  
- 44 -	GM Left_fasciculus-dorsolateralis	
- 45 -	GM Right_reticular-formation	 		
- 46 -	GM Right_dorsomarginal-nucleus	  
- 47 -	GM Right_fasciculus-dorsolateralis
- 48 -	central-canal	     			    	    
- 49 -	CSF contour	 		            	    

**Combined labels**
- 50  -  GM Left_ventral-horn, 32:34
- 51  -  GM Right_ventral-horn, 35:37
- 52  -  GM Left_intermediate-zone, 38:39
- 53  -  GM Right_intermediate-zone, 40:41
- 54  -  GM Left_dorsal-horn, 42:44
- 55  -  GM Right_dorsal-horn, 45:47
- 56  -  spinal-cord, 0:48
- 57  -  white-matter, 0:31
- 58  -  gray-matter, 32:48
- 59  -  dorsal-columns, 0:3
- 60  -  lateral-funiculi, 4:13
- 61  -  ventral-funiculi, 14:29

The intensities of each label in `atlas/AMU7T_50_labels.nii.gz` are detailed [here](https://github.com/spinalcordtoolbox/template_AMU7T/blob/nl/AMU7Tv3/atlas/Label_intensities_description.txt), and the parcellation can be visualized with this Lookup table in [FSLeyes](https://github.com/spinalcordtoolbox/template_AMU7T/files/12033959/AMU7T_parc.txt) and [ITK-SNAP](https://github.com/spinalcordtoolbox/template_AMU7T/files/12033957/AMU7T_parc_itk.txt)

## Usage: Registration of AMU7T to Subject space
For an optimal registration of the AMU7T, it is recommended to work with a WM mask that covers the dorsal horns up to the CSF (see the the animation below).

![WM_seg](https://github.com/spinalcordtoolbox/template_AMU7T/assets/77469192/3051e1c9-1e77-4949-82eb-2ebf73e7ef89)

### Optimal parameters for register AMU7T to subject space
```
sct_register_to_template -i image.nii.gz -s image_wm.nii.gz -l landmarks.nii.gz -c t1 -v 1 -s-template-id 4  -t ../template_AMU7T  -param step=1,type=imseg,algo=centermassrot,rot_method=pcahog:step=2,type=seg,algo=bsplinesyn,slicewise=0,metric=MeanSquares,samplStrategy=None,samplPercent=0.2,iter=2,smooth=1,rot_method=pcahog:step=3,type=seg,algo=syn,metric=MeanSquares,shrink=2,dof=Tz_Rz_Sz,slicewise=1,iter=20 -ref subject
```

### Atlas registration to subject space
```
sct_apply_transfo -i template_AMU7T/atlas/AMU7T_50_labels.nii.gz -d image.nii.gz -w warp_template2anat.nii.gz -o labels_AMU7T2anat.nii.gz -x nn
```

### Other uses with SCT commands 
```
sct_warp_template -d image.nii.gz -w warp_template2anat.nii.gz  -t template_AMU7T
sct_extract_metric -i image.nii.gz -f label\atlas  -method wa -o wa_T1.csv -z 9:32 -perslice 1
```



## Related issues
[#13](https://github.com/spinalcordtoolbox/PAM50/issues/13) 
[#4](https://github.com/spinalcordtoolbox/template_AMU7T/issues/4)
[#PR14](https://github.com/spinalcordtoolbox/PAM50/pull/14)

## How to cite
Le Troter, A., Laines Medina, N., Mchinda, S., Cohen-Adad, J., & Callot, V. (June 2023). [AMU7T : a 3D qT1 and T2*w high-resolution in vivo template with refined white and gray matter parcellation dedicated to 7T spinal cord MR analyses](https://github.com/spinalcordtoolbox/template_AMU7T/files/12031127/AMU7T.a.3D.qT1.and.T2s.w.high-resolution.in.vivo.template.with.refined.white.and.gray.matter.parcellation.dedicated.to.7T.spinal.cord.MR.analyses.pdf) [Oral presentation - p. 0569]. ISMRM & ISMRT annual Meeting & Exhibition, Toronto, ON, Canada.
