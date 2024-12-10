import tempfile
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
intervals = snakemake.params.get("intervals")


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk SelectVariants"
        " -V gendb://{snakemake.input.database}"
        " --reference {snakemake.input.reference}"
        " --intervals {intervals}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.vcf}"
        " {log}"
    )