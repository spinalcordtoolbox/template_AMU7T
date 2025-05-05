# AMU7T: 3D qT1 and T2*w in vivo template + atlas
AMU7T : high-resolution multimodal quantitative T1 and T2*-weighted templates with white and gray matter spinal cord and substructures atlas, aligned with the PAM50 space
![AMU_7T_template](https://github.com/spinalcordtoolbox/template_AMU7T/assets/77469192/3b5cb4b8-5931-4841-b952-d968f4b4338f)

## Main Dependencies
[![SCT](https://img.shields.io/badge/SCT-7.0-green)](https://github.com/spinalcordtoolbox/spinalcordtoolbox/releases/tag/7.0)

## Data
This data repository contains:
- `template/AMU26_qt1.nii.gz`: 7T qT1 template from 26 subjects.
- `template/AMU72_t2s.nii.gz`: 7T T2*w template from 72 subjects.
- `template/AMU7T_gm.nii.gz`: Probabilistic gray matter mask.
- `template/AMU7T_wm.nii.gz`: Probabilistic white matter mask.
- `template/AMU7T_sc.nii.gz`: Probabilistic spinal cord mask.
- `template/AMU7T_levels.nii.gz`: SC mask with discrete vertebral levels.
- `atlas/AMU7T_50_labels.nii.gz`: Atlas with 50 labels (WM parcels from [Lévy et al., NeuroImage (2015)](https://pubmed.ncbi.nlm.nih.gov/26099457/), and GM parcels derivated from _Hausman, _L. Atlases of the Spinal Cord and Brainstem and the Forebrain. (Thomas, 1962)__
- `atlas/AMU7T_atlas_ID_bin.nii.gz`: Binary masks by ID.

### Multilabel atlas containing:

<details>
  <summary> atlas/ </summary>
  
| **ID** | **Region**                               |
|--------|------------------------------------------|
| 0      | WM Left_fasciculus-gracilis              |
| 1      | WM Right_fasciculus-gracilis             |
| 2      | WM Left_fasciculus-cuneatus              |
| 3      | WM Right_fasciculus-cuneatus             |
| 4      | WM Left_lateral-corticospinal            |
| 5      | WM Right_lateral-corticospinal           |
| 6      | WM Left_ventral-spinocerebellar          |
| 7      | WM Right_ventral-spinocerebellar         |
| 8      | WM Left_rubrospinal                      |
| 9      | WM Right_rubrospinal                     |
| 10     | WM Left_lateral-reticulospinal           |
| 11     | WM Right_lateral-reticulospinal          |
| 12     | WM Left_spinal-lemniscus-spinothalamic   |
| 13     | WM Right_spinal-lemniscus-spinothalamic  |
| 14     | WM Left_spino-olivary                    |
| 15     | WM Right_spino-olivary                   |
| 16     | WM Left_ventrolateral-reticulospinal     |
| 17     | WM Right_ventrolateral-reticulospinal    |
| 18     | WM Left_lateral-vestibulospinal          |
| 19     | WM Right_lateral-vestibulospinal         |
| 20     | WM Left_ventral-reticulospinal           |
| 21     | WM Right_ventral-reticulospinal          |
| 22     | WM Left_ventral-corticospinal            |
| 23     | WM Right_ventral-corticospinal           |
| 24     | WM Left_tectospinal                      |
| 25     | WM Right_tectospinal                     |
| 26     | WM Left_medial-reticulospinal            |
| 27     | WM Right_medial-reticulospinal           |
| 28     | WM Left_medial-longitudinal-fasciculus   |
| 29     | WM Right_medial-longitudinal-fasciculus  |
| 30     | anterior-fissure                         |
| 31     | septum                                   |
| 32     | GM Left_medial-ventral-horn              |
| 33     | GM Left_central-ventral-horn             |
| 34     | GM Left_lateral-ventral-horn             |
| 35     | GM Right_medial-ventral-horn             |
| 36     | GM Right_central-ventral-horn            |
| 37     | GM Right_lateral-ventral-horn            |
| 38     | GM Left_dorsal-intermediate-zone         |
| 39     | GM Left_ventral-intermediate-zone        |
| 40     | GM Right_dorsal-intermediate-zone        |
| 41     | GM Right_ventral-intermediate-zone       |
| 42     | GM Left_reticular-formation              |
| 43     | GM Left_dorsomarginal-nucleus            |
| 44     | GM Left_fasciculus-dorsolateralis        |
| 45     | GM Right_reticular-formation             |
| 46     | GM Right_dorsomarginal-nucleus           |
| 47     | GM Right_fasciculus-dorsolateralis       |
| 48     | central-canal                            |
| 49     | CSF contour                              |

**Combined labels**
| **ID** | **Region**                               |
|--------|------------------------------------------|
| 50     | GM Left_ventral-horn, 32:34              |
| 51     | GM Right_ventral-horn, 35:37             |
| 52     | GM Left_intermediate-zone, 38:39         |
| 53     | GM Right_intermediate-zone, 40:41        |
| 54     | GM Left_dorsal-horn, 42:44               |
| 55     | GM Right_dorsal-horn, 45:47              |
| 56     | spinal-cord, 0:48                       |
| 57     | white-matter, 0:31                      |
| 58     | gray-matter, 32:48                      |
| 59     | dorsal-columns, 0:3                     |
| 60     | lateral-funiculi, 4:13                  |
| 61     | ventral-funiculi, 14:29                 |


</details>

#### Note :
- List of clases on `atlas/AMU7T_50_labels.nii.gz` is detailed [here](https://github.com/spinalcordtoolbox/template_AMU7T/blob/main/atlas/Label_intensities_description.txt), 
- For a good visualization of parcellations use these LookUp Tables : [FSLeyes](https://github.com/spinalcordtoolbox/template_AMU7T/files/12033959/AMU7T_parc.txt), [ITK-SNAP](https://github.com/spinalcordtoolbox/template_AMU7T/files/12033957/AMU7T_parc_itk.txt)


## Usage: 
### 1. Automatic segmentations and vertebral labeling using `sct_deepseg`  

**SC segmentation: [`spinalcord`](https://github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord) model**
```
sct_deepseg spinalcord -install
```
```
sct_deepseg spinalcord -i IMAGE.nii.gz  -o IMAGE_sc_seg.nii.gz
```

**GM segmentation: [`graymatter`](https://github.com/ivadomed/model-gm-contrast-region-agnostic) model**
```
sct_deepseg graymatter -install
```
```
sct_deepseg graymatter -i IMAGE.nii.gz  -o IMAGE_gm_seg.nii.gz 
```
**WM segmentation:**
```
sct_maths -i IMAGE_sc_seg.nii.gz -sub IMAGE_gm_seg.nii.gz  -o IMAGE_wm_seg.nii.gz
```
:warning: **Warning:** Manually correct WM segmentation if necessary.

**Vertebral labeling: [`totalspineseg`](https://github.com/neuropoly/totalspineseg) model**
```
sct_deepseg totalspineseg -install
```
```
sct_deepseg totalspineseg -i IMAGE.nii.gz  -step 1 -o  IMAGE_total.nii.gz
```

### 2. AMU7T Registration 
#### 2.1 Registration of Template to Subject space
```console
sct_register_to_template
        -i IMAGE.nii.gz
        -s IMAGE_wm_seg.nii.gz
        -ldisc IMAGE_total_step_1_levels.nii.gz
        -t $template_AMU7T_path
        -c t1
        -s-template-id 4
        -ref subject 
        -param step=0,type=label,algo=syn,rot_method=pca,dof=Tx_Ty_Tz_Rz:
              step=1,type=imseg,algo=centermassrot,rot_method=pcahog:
              step=2,type=seg,algo=bsplinesyn,slicewise=0,metric=MeanSquares,samplStrategy=None,samplPercent=0.2,iter=3,smooth=1,rot_method=pca:
              step=3,type=seg,algo=syn,metric=MeanSquares,shrink=2,dof=Tz_Rz_Sz,slicewise=1,iter=20
        -ofolder AMU7T_2_IMAGE
```

#### 2.2. Registration of Atlas

**Warp template and all atlases to Subject space**
```console
sct_warp_template
        -d IMAGE.nii.gz
        -w AMU7T_2_IMAGE/warp_template2anat.nii.gz
        -t $template_AMU7T_path
        -ofolder AMU7T_2_IMAGE
```

**Warp multilabel atlas**
```console
sct_apply_transfo
        -i $template_AMU7T_path/atlas/AMU7T_50_labels.nii.gz
        -d IMAGE.nii.gz
        -w AMU7T_2_IMAGE/warp_template2anat.nii.gz
        -x nn
        -o AMU7T_2_IMAGE/AMU7T_50_labels_2_IMAGE.nii.gz
```

#### 2.3 Extract quantitative metrics
```console
sct_extract_metric
        -i IMAGE.nii.gz
        -f AMU7T_2_IMAGE/label/atlas
        -method wa
        -z 2:17
        -perslice 1
        -o AMU7T_2_IMAGE/IMAGE_wa_T1.csv
```

## How to cite
Le Troter, A., Laines Medina, N., Mchinda, S., Cohen-Adad, J., & Callot, V. (June 2023). [AMU7T : a 3D qT1 and T2*w high-resolution in vivo template with refined white and gray matter parcellation dedicated to 7T spinal cord MR analyses](https://github.com/spinalcordtoolbox/template_AMU7T/files/12031127/AMU7T.a.3D.qT1.and.T2s.w.high-resolution.in.vivo.template.with.refined.white.and.gray.matter.parcellation.dedicated.to.7T.spinal.cord.MR.analyses.pdf) [Oral presentation - p. 0569]. ISMRM & ISMRT annual Meeting & Exhibition, Toronto, ON, Canada.
