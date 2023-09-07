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

### Labels
Multilabel atlas in in `atlas/AMU7T_50_labels.nii.gz` containing:

**ID    Region						                File			            Label in atlas/AMU7T_50_labels.nii.gz**
- 0	    WM_Left_fasciculus-gracilis		            AMU7T_label_00_bin.nii.gz	    39
- 1	    WM_Right_fasciculus-gracilis	         	AMU7T_label_01_bin.nii.gz	    1
- 2	    WM_Left_fasciculus-cuneatus			        AMU7T_label_02_bin.nii.gz	    2
- 3	    WM_Right_fasciculus-cuneatus	 	    	AMU7T_label_03_bin.nii.gz	    3
- 4	    WM_Left_lateral-corticospinal	 	        AMU7T_label_04_bin.nii.gz	    4   
- 5	    WM_Right_lateral-corticospinal	 	    	AMU7T_label_05_bin.nii.gz	    5
- 6	    WM_Left_ventral-spinocerebellar	 	        AMU7T_label_06_bin.nii.gz	    6
- 7	    WM_Right_ventral-spinocerebellar	        AMU7T_label_07_bin.nii.gz	    7
- 8	    WM_Left_rubrospinal	 			            AMU7T_label_08_bin.nii.gz	    8
- 9	    WM_Right_rubrospinal	 		            AMU7T_label_09_bin.nii.gz	    9
- 10	WM_Left_lateral-reticulospinal	 	        AMU7T_label_10_bin.nii.gz	    10
- 11	WM_Right_lateral-reticulospinal	 	        AMU7T_label_11_bin.nii.gz	    11
- 12	WM_Left_spinal-lemniscus-spinothalamic	 	AMU7T_label_12_bin.nii.gz	    12
- 13	WM_Right_spinal-lemniscus-spinothalamic	    AMU7T_label_13_bin.nii.gz	    13
- 14	WM_Left_spino-olivary	 	            	AMU7T_label_14_bin.nii.gz	    14
- 15	WM_Right_spino-olivary	            		AMU7T_label_15_bin.nii.gz	    15
- 16	WM_Left_ventrolateral-reticulospinal    	AMU7T_label_16_bin.nii.gz	    16
- 17	WM_Right_ventrolateral-reticulospinal	    AMU7T_label_17_bin.nii.gz	    17
- 18	WM_Left_lateral-vestibulospinal	     	    AMU7T_label_18_bin.nii.gz	    18
- 19	WM_Right_lateral-vestibulospinal	     	AMU7T_label_19_bin.nii.gz	    19
- 20	WM_Left_ventral-reticulospinal	 		    AMU7T_label_20_bin.nii.gz	    20
- 21	WM_Right_ventral-reticulospinal	 	        AMU7T_label_21_bin.nii.gz	    21  
- 22	WM_Left_ventral-corticospinal	 		    AMU7T_label_22_bin.nii.gz	    22
- 23	WM_Right_ventral-corticospinal	 		    AMU7T_label_23_bin.nii.gz	    23
- 24	WM_Left_tectospinal	 			            AMU7T_label_24_bin.nii.gz	    24
- 25	WM_Right_tectospinal	 			        AMU7T_label_25_bin.nii.gz	    25
- 26	WM_Left_medial-reticulospinal	 	    	AMU7T_label_26_bin.nii.gz	    26
- 27	WM_Right_medial-reticulospinal	 	    	AMU7T_label_27_bin.nii.gz	    27
- 28	WM_Left_medial-longitudinal-fasciculus	 	AMU7T_label_28_bin.nii.gz	    28
- 29	WM_Right_medial-longitudinal-fasciculus     AMU7T_label_29_bin.nii.gz	    29
- 30	anterior-fissure	 			            AMU7T_label_30_bin.nii.gz	    76
- 31	septum	 					                AMU7T_label_31_bin.nii.gz	    100
- 32	GM_Left_medial-ventral-horn	 		        AMU7T_label_32_bin.nii.gz	    43
- 33	GM_Left_central-ventral-horn    		    AMU7T_label_33_bin.nii.gz	    45
- 34	GM_Left_lateral-ventral-horn	     		AMU7T_label_34_bin.nii.gz	    44
- 35	GM_Right_medial-ventral-horn	 	    	AMU7T_label_35_bin.nii.gz	    41
- 36	GM_Right_central-ventral-horn	 		    AMU7T_label_36_bin.nii.gz	    42
- 37	GM_Right_lateral-ventral-horn	     		AMU7T_label_37_bin.nii.gz	    40
- 38	GM_Left_dorsal-intermediate-zone	     	AMU7T_label_38_bin.nii.gz	    32
- 39	GM_Left_ventral-intermediate-zone	 	    AMU7T_label_39_bin.nii.gz	    53
- 40	GM_Right_dorsal-intermediate-zone	    	AMU7T_label_40_bin.nii.gz	    33
- 41	GM_Right_ventral-intermediate-zone	    	AMU7T_label_41_bin.nii.gz	    51
- 42	GM_Left_reticular-formation	 		        AMU7T_label_42_bin.nii.gz	    34
- 43	GM_Left_dorsomarginal-nucleus	 	    	AMU7T_label_43_bin.nii.gz	    46
- 44	GM_Left_fasciculus-dorsolateralis	 	    AMU7T_label_44_bin.nii.gz	    54
- 45	GM_Right_reticular-formation	 		    AMU7T_label_45_bin.nii.gz	    35
- 46	GM_Right_dorsomarginal-nucleus	    		AMU7T_label_46_bin.nii.gz	    47
- 47	GM_Right_fasciculus-dorsolateralis	     	AMU7T_label_47_bin.nii.gz	    52
- 48	central-canal	     			    	    AMU7T_label_48_bin.nii.gz	    74
- 49	CSF-contour	 		            	    	AMU7T_label_49_bin.nii.gz	    72

**Combined labels**
- 50    GM_Left_ventral-horn, 32:34
- 51    GM_Right_ventral-horn, 35:37
- 52    GM_Left_intermediate-zone, 38:39
- 53    GM_Right_intermediate-zone, 40:41
- 54    GM_Left_dorsal-horn, 42:44
- 55    GM_Right_dorsal-horn, 45:47
- 56    spinal-cord, 0:48
- 57    white-matter, 0:31
- 58    gray-matter, 32:48
- 59    dorsal-columns, 0:3
- 60    lateral-funiculi, 4:13
- 61    ventral-funiculi, 14:29

The intensities of each label in `atlas/AMU7T_50_labels.nii.gz` are detailed [here](https://github.com/spinalcordtoolbox/template_AMU7T/blob/nl/AMU7Tv3/atlas/Label_intensities_description.txt), and the parcellation can be visualized with this Lookup table in [FSLeyes](https://github.com/spinalcordtoolbox/template_AMU7T/files/12033959/AMU7T_parc.txt) and [ITK-SNAP](https://github.com/spinalcordtoolbox/template_AMU7T/files/12033957/AMU7T_parc_itk.txt)

## Related issues
[#13](https://github.com/spinalcordtoolbox/PAM50/issues/13) 
[#4](https://github.com/spinalcordtoolbox/template_AMU7T/issues/4)
[#PR14](https://github.com/spinalcordtoolbox/PAM50/pull/14)

## How to cite
Le Troter, A., Laines Medina, N., Mchinda, S., Cohen-Adad, J., & Callot, V. (June 2023). [AMU7T : a 3D qT1 and T2*w high-resolution in vivo template with refined white and gray matter parcellation dedicated to 7T spinal cord MR analyses](https://github.com/spinalcordtoolbox/template_AMU7T/files/12031127/AMU7T.a.3D.qT1.and.T2s.w.high-resolution.in.vivo.template.with.refined.white.and.gray.matter.parcellation.dedicated.to.7T.spinal.cord.MR.analyses.pdf) [Oral presentation - p. 0569]. ISMRM & ISMRT annual Meeting & Exhibition, Toronto, ON, Canada.
