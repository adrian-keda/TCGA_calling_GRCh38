# TCGA_calling_GRCh38

This github repository has the code used to download, call and annotate variants from TCGA WES data following GATK's best practices. Brief description of the content included in each folder:

- Download_Calling: snakemake script and config file used to download data from GDC and call variants using GATK's HaplotypeCaller.

- Envs: list of conda environments used in the snakemake scripts.

- GENOMICS_DB: code to create the genomics databases using GenomicsDBImport tool.

- Joint_Genotyping: code to perform joint genotyping (merging all samples information into a single vcf file).

- Resources: folder with some resources used in this process (TCGA's sample manifest, a sample mapping file and a list of gencode's transcripts).

- Variant_Recallibration: code to apply Variant Recalibration on called snps and indels.

- VEP_annotation: code to annotate called variants using Ensembl's VEP.

Some additional resources not provided in this repository were downloaded:

- TCGA human reference genome, you can find it [here](https://gdc.cancer.gov/about-data/gdc-data-processing/gdc-reference-files).

- Resources needed for Variant Recalibration were downloaded from GATK's [resource bundle](https://gatk.broadinstitute.org/hc/en-us/articles/360035890811-Resource-bundle).

- VEP version 113 was downloaded and installed using a conda environment. AlphaMissense, dbNSFP, REVEL and SpliceAI plugins were downloaded an prepared according to [VEP's intallation guide](https://www.ensembl.org/info/docs/tools/vep/script/vep_download.html). Additionally, ClinVar was downloaded from its [FTP site](https://www.ncbi.nlm.nih.gov/clinvar/).