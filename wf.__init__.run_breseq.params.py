"""Run `latch launch wf.__init__.run_breseq.params.py` to launch this workflow"""

from latch.types import LatchDir

params = {
    "_name": "wf.__init__.run_breseq", # Don't edit this value.
    "data_folder": LatchDir("latch:///MaxKat-sequencing/JN2"), # DEFAULT. <class 'latch.types.directory.LatchDir'>
    "output_directory": LatchDir("latch://MaxKat-sequencing/JN2/results"), # DEFAULT. <class 'latch.types.directory.LatchDir'>
}