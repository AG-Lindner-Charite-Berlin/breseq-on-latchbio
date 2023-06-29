"""
Minimal template workflow to show how to run workflows that use docker in Latch

For a more comprehensive template, see the assemble_and_sort workflow
For examples on how to use docker in Latch, see https://docs.latch.bio/examples/workflows_examples.html
"""

from wf.task import breseq_task

from latch.resources.launch_plan import LaunchPlan
from latch.resources.workflow import workflow
from latch.types.directory import LatchOutputDir, LatchDir
from latch.types.file import LatchFile
from latch.types.metadata import LatchAuthor, LatchMetadata, LatchParameter, LatchRule

metadata = LatchMetadata(
    display_name="breseq",
    author=LatchAuthor(
        name="Timon Schneider",
    ),
    parameters={
        "data_folder": LatchParameter(
            display_name="Folder containing data",
        ),
        "output_directory": LatchParameter(
            display_name="Output Directory",
            batch_table_column=True,  # Show this parameter in batched mode.
        ),
    },
    tags=[],
)


@workflow(metadata)
def run_breseq(
    data_folder: LatchDir,
    output_directory: LatchOutputDir,
) -> LatchFile:
    return breseq_task(data_folder=data_folder, output_directory=output_directory)


LaunchPlan(
    run_breseq,
    "Test Data",
    {
        "data_folder": LatchDir("latch:///MaxKat-sequencing/JN2"),
        "output_directory": LatchOutputDir("latch://MaxKat-sequencing/JN2/results"),
    },
)
