import pandas as pd 

from qiime2.metadata.metadata import Metadata, CategoricalMetadataColumn
from qiime2.sdk import Artifact, PluginManager, Result

pm = PluginManager()
demux_plugin = pm.plugins['demux']
demux_summarize = demux_plugin.actions['summarize']
pm.plugins


print(demux_summarize.description)
demux_summarize_signature = demux_summarize.signature
print(demux_summarize_signature.inputs)
print(demux_summarize_signature.parameters)
print(demux_summarize_signature.outputs)

# +
seqs1 = Result.load('fmt-tutorial-demux-1-10p.qza')
sum_data = demux_summarize(seqs1)

sum_data.visualization
