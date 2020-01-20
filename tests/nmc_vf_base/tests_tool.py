# import nmc_verification.nmc_vf_base.tool as tool
# import batch_test.nmc_vf_base.read_write_jumpe as rwj
# if __name__ == '__main__':
#
#     tool.copy_tools.copy_m4_to_nc(input_root_dir='../data/m4_data',output_root_dir='../data/output')
#     file_list = tool.path_tools.get_filename_list_in_dir('../data/output')
#     for filepath in file_list:
#         rwj.file_is_exist()

import nmc_verification.nmc_vf_base as nvb
import matplotlib.colors as colors
cmap = [[255,255,255],[0,255,0],[0,128,0],[0,128,128],[0,0,255],[0,0,128],[128,0,128],[255,0,0],[128,0,0],[128,128,0]]
cmap = colors.ListedColormap(cmap, 'indexed')
nvb.color_tools.show_cmap_clev(cmap)