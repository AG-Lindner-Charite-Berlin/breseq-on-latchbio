import os
import subprocess
from pathlib import Path
from typing import List

from latch.functions.messages import message
from latch.resources.tasks import small_task
from latch.types.directory import LatchOutputDir, LatchDir
from latch.types.file import LatchFile


def run(cmd: List[str]):
    import os

    try:
        return os.system(" ".join(cmd))
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode("utf-8")
        if stderr != "":
            message(
                "error",
                {"title": "Blastp Failed", "body": f"Stderr: {stderr}"},
            )
        print(stderr)
        raise e


@small_task
def breseq_task(
    data_folder: LatchDir,
    output_directory: LatchOutputDir,
) -> LatchFile:
    # breseq_cmd = [
    #     "docker",
    #     "run",
    #     "--user",
    #     "root",  # run as root to avoid permission issues
    #     "-v",
    #     f"{database_path.parent}:/data/",  # mount the database file directory into the container
    #     "ummidock/breseq",
    #     "makeblastdb",
    #     "-in",
    #     f"/data/{database_path.name}",
    #     "-dbtype",
    #     "prot",
    # ]

    data_path = Path(data_folder.local_path)

    print("data_path.name", data_path.name)

    breseq_cmd = [
        "docker",
        "run",
        "--name",
        "breseq-container",
        "--user",
        "root",
        "-v",
        f"{data_path.name}:/data/",
        "ummidock/breseq:0.32.1",
        "breseq",
        "--reference",
        f"/data/reference.gbk",
        "--name",
        "sample",
        "-j",
        "8",
        "--output",
        f"/data/results",
        "/data/read1.fastq.gz",
        "/data/read2.fastq.gz",
    ]

    breseq_run = run(breseq_cmd)

    print(os.system("docker logs breseq-container"))

    print(os.system("ls -l"))

    return LatchFile(
        "/data/results/index.html", f"{output_directory.remote_directory}/index.html"
    )
