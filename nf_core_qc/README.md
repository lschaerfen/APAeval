# Pilot: Mapping reads with nf-core/rnaseq

For the pilot, the **P19 SRSF3** samples are used. 

Download the SRA samples specified in `data/run_identifiers.txt` and fill in the full paths to these FASTQ files in `data/samplesheet.csv`. 

## On a linux machine with Singularity installed

Create a conda environment with

``` bash
conda env create -f envs/requirements.yaml
conda activate apa-eval
```

In order to avoid a warning, set the environment variable `NXF_SINGULARITY_CACHEDIR` to a directory of your choice (e.g. `/tmp`).

Adjust max memory and max CPU settings in `nf_core/run_rnaseq.sh`.

Run the rnaseq pipeline with

``` bash
cd nf_core
bash run_rnaseq.sh
```