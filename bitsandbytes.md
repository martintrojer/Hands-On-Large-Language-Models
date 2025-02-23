## bitsandbytes ROCm support

in the bitsandbytes submodule

cmake -DCOMPUTE_BACKEND=hip -S .  # Use -DBNB_ROCM_ARCH="gfx90a;gfx942" to target specific gpu arch
make

and then we do

uv pip install bitsandbytes
