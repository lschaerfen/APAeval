#!/bin/bash
nextflow run nf-core/rnaseq \
    -r 2.0 \
    --input data/samplesheet.csv \
    --genome GRCm38 \
    -profile singularity \
    --max_memory '30.GB' --max_cpus 10
