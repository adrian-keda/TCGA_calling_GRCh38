import os
import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
sample_map = snakemake.input.sample_map


db_action = snakemake.params.get("db_action", "create")
if db_action == "create":
    db_action = "--genomicsdb-workspace-path"
elif db_action == "update":
    db_action = "--genomicsdb-update-workspace-path"
else:
    raise ValueError(
        "invalid option provided to 'params.db_action'; please choose either 'create' or 'update'."
    )


intervals = snakemake.input.get("intervals")
if not intervals:
    intervals = snakemake.params.get("intervals")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk GenomicsDBImport"
        " --reader-threads {snakemake.threads}"
        " --sample-name-map {sample_map}"
        " --intervals {intervals}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " {db_action} {snakemake.output.db}"
        " {log}"
    )