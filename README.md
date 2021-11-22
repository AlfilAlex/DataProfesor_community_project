# DataProfesor_community_project
Community project to find molecules with activity against B-lactamase. In this analisys I re-downloaded the files from ChEMBL and analysed them.

The file called **lactamase_dataprof_community_project.ipynb** is the merge of all the files numered.

## Data directly download from ChEMBL
After several trys, I found imposible to train a model with the given data, so I downloaded dirctly from the ChEMBL. After that, I tried to do the same as with the files given by the Data Profesor, but I did not succes too. By reading in literature i found a pipeline where theh first split into actives and inactives was given by a particular column called *Comment*.

## Models
Using the pipeline mentioned above I was able to train a DNN model an a GNN model. The GNN was implemented with deepchem package, but I also had implemented it with Pytorch Geometric with the files given by the professor. I have plans to train these model too with the last dataset but is still a TODO. 

## It is my first chemoinformatics project
This is my first project of chemoinformatics, so I dont know if I missed something, so comments about my work (others than typos, wich may be a loooot) are very interesting for me.
