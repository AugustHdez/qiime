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

# +
seqs2 = Result.load('fmt-tutorial-demux-2-10p.qza')
sum_data2 = demux_summarize(seqs2)

print(dir(sum_data2))
print(type(sum_data2.visualization))
sum_data2.visualization

# +
dada2_plugin = pm.plugins['dada2']
dada2_denoise_single = dada2_plugin.actions['denoise_single']

quality_control1 = dada2_denoise_single(
    demultiplexed_seqs = seqs1,
    trunc_len =150,
    trim_left = 13
)

quality_control2 = dada2_denoise_single(
    demultiplexed_seqs = seqs2,
    trunc_len = 150,
    trim_left = 13
)

# -

metadata_plugin = pm.plugins['metadata']
metadata_tabulate = metadata_plugin.actions['tabulate']

stats_metadata1 = metadata_tabulate(
    input=quality_control1.denoising_stats.view(Metadata)
                                   )
stats_metadata1.visualization

stats_metadata2 = metadata_tabulate(
    input=quality_control2.denoising_stats.view(Metadata)
                                    )
stats_metadata2.visualization
