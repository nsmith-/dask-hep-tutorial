from dask.sizeof import sizeof
import uproot
import awkward


@sizeof.register(awkward.highlevel.Array)
def sizeof_ak_generic(obj):
    return obj.nbytes


@sizeof.register(uproot.model.Model)
def sizeof_uproot_generic(obj):
    return obj.num_bytes
