# AMU7T: 3D qT1 and T2*s in vivo template + atlas
![AMU_7T_template](https://github.com/spinalcordtoolbox/template_AMU7T/assets/77469192/3b5cb4b8-5931-4841-b952-d968f4b4338f)

## Data
This data repository contains:
- `template/AMU26_qt1.nii.gz`: 7T qT1 template from 26 subjects.
- `template/AMU72_t2s.nii.gz`: 7T T2*w template from 72 subjects.
- `template/AMU7T_gm.nii.gz`: Probabilistic gray matter mask.
- `template/AMU7T_wm.nii.gz`: Probabilistic white matter mask.
- `template/AMU7T_sc.nii.gz`: Probabilistic spinal cord mask.
- `atlas/AMU7T_50_labels.nii.gz`: Atlas with 50 labels (WM parcels from [Levi et al., NeuroImage (2015)](https://pubmed.ncbi.nlm.nih.gov/26099457/)., and GM parcels derivated from _Hausman, _L. Atlases of the Spinal Cord and Brainstem and the Forebrain. (Thomas, 1962).__
- `atlas/AMU7T_label_ID_bin.nii.gz`: Binary masks by ID.

### Labels
Multilabel atlas in in `atlas/AMU7T_50_labels.nii.gz` containing:

**ID (compatible with PAM50 ID)	- Name**
- 0	- WM	Left	fasciculus-gracilis 
- 1	- WM	Right	fasciculus-gracilis 
- 2	- WM	Left	fasciculus-cuneatus
- 3	- WM	Right	fasciculus-cuneatus
- 4	- WM	Left	lateral-corticospinal-tract
- 5 -	WM	Right	lateral-corticospinal-tract
- 6 -	WM	Left	ventral-spinocerebellar-tract
- 7 - WM	Right	ventral-spinocerebellar-tract
- 8	- WM	Left	rubrospinal-tract
- 9	- WM	Right	rubrospinal-tract
- 10	- WM	Left	lateral-reticulospinal-tract
- 11	- WM	Right	lateral-reticulospinal-tract
- 12	- WM	Left	spinal-lemniscus-spinothalamic
- 13	- WM	Right	spinal-lemniscus-spinothalamic
- 14	- WM	Left	spino-olivary-tract
- 15	- WM	Right	spino-olivary-tract
- 16	- WM	Left	ventrolateral-reticulospinal-tract
- 17	- WM	Right	ventrolateral-reticulospinal-tract
- 18	- WM	Left	lateral-vestibulospinal-tract
- 19	- WM	Right	lateral-vestibulospinal-tract
- 20	- WM	Left	ventral-reticulospinal-tract
- 21	- WM	Right	ventral-reticulospinal-tract
- 22	- WM	Left	ventral-corticospinal-tract
- 23	- WM	Right	ventral-corticospinal-tract
- 24	- WM	Left	tectospinal-tract
- 25	- WM	Right	tectospinal-tract
- 26	- WM	Left	medial-reticulospinal-tract
- 27	- WM	Right	medial-reticulospinal-tract
- 28	- WM	Left	medial-longitudinal-fasciculus
- 29	- WM	Right	medial-longitudinal-fasciculus
- 301	- GM	Left	medial-ventral-horn
- 302	- GM	Left	central-ventral-horn
- 303	- GM	Left	lateral-ventral-horn
- 311	- GM	Right	medial-ventral-horn
- 312	- GM	Right	central-ventral-horn
- 313	- GM	Right	lateral-ventral-horn
- 321	- GM	Left	intermediate-zone
- 322	- GM	Left	ventral-intermediate-zone
- 331	- GM	Right	intermediate-zone
- 332	- GM	Right	ventral-intermediate-zone
- 341 -	GM	Left	reticular-formation
- 342	- GM	Left	dorsomarginal-nucleus
- 343	- GM	Left	fasciculus-dorsolateralis
- 351	- GM	Right	reticular-formation
- 352	- GM	Right	dorsomarginal-nucleus
- 353	- GM	Right	fasciculus-dorsolateralis
- 36  - CSF	contour
- 37	- Central-zone
- 38	- Anterior-fissure
- 39	- Septum

**Combined labels**
- 30	- GM left ventral horn    -    301:303
- 31	- GM right ventral horn   -    311:313
- 32	- GM left intermediate zone -  321:322
- 33	- GM right intermediate zone - 331:332
- 34	- GM left dorsal horn      -   341:343
- 35	- GM right dorsal horn     -   351:353
- 50	- Spinal cord              -   0:353
- 51	- White matter            -    0:29
- 52	- Gray matter             -    301:353
- 53	- Dorsal columns          -    0:3
- 54	- Lateral funiculi        -    4:13
- 55	- Ventral funiculi        -    14:29

The intensities of each label in `atlas/AMU7T_50_labels.nii.gz` are detailed here, and the parcellation can be visualized with this Lookup table in [FSLeyes](https://github.com/spinalcordtoolbox/template_AMU7T/files/12033959/AMU7T_parc.txt) and [ITK-SNAP](https://github.com/spinalcordtoolbox/template_AMU7T/files/12033957/AMU7T_parc_itk.txt)

## Related issues
[#13](https://github.com/spinalcordtoolbox/PAM50/issues/13) 
[#4147](https://github.com/spinalcordtoolbox/spinalcordtoolbox/issues/4147)
[#PR14](https://github.com/spinalcordtoolbox/PAM50/pull/14)

## How to cite
Le Troter, A., Laines Medina, N., Mchinda, S., Cohen-Adad, J., & Callot, V. (June 2023). [AMU7T : a 3D qT1 and T2*w high-resolution in vivo template with refined white and gray matter parcellation dedicated to 7T spinal cord MR analyses](https://github.com/spinalcordtoolbox/template_AMU7T/files/12031127/AMU7T.a.3D.qT1.and.T2s.w.high-resolution.in.vivo.template.with.refined.white.and.gray.matter.parcellation.dedicated.to.7T.spinal.cord.MR.analyses.pdf) [Oral presentation]. ISMRM & ISMRT annual Meeting & Exhibition, Toronto, ON, Canada.
