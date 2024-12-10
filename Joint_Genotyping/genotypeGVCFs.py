import os
import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
intervals = snakemake.input.get("intervals")
if not intervals:
    intervals = snakemake.params.get("intervals")
if intervals:
    intervals = "--intervals {}".format(intervals)


# Allow for either an input gvcf or GenomicsDB
gvcf = snakemake.input.get("gvcf")
genomicsdb = snakemake.input.get("genomicsdb")
if gvcf:
    if genomicsdb:
        raise Exception("Only input.gvcf or input.genomicsdb expected, got both.")
    input_string = gvcf
else:
    if genomicsdb:
        input_string = "gendb://{}".format(genomicsdb)
    else:
        raise Exception("Expected input.gvcf or input.genomicsdb.")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk GenotypeGVCFs"
        " --variant {input_string}"
        " --reference {snakemake.input.ref}"
        " {intervals}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.vcf}"
        " {log}"
    )
