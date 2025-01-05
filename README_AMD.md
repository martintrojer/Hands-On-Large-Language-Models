1.

Install RoCm

2.

export HIPCXX="$(hipconfig -l)/clang"
export HIP_PATH="$(hipconfig -R)"

3.

venv/bin/pip uninstasll llama_cpp_python

CMAKE_ARGS="-DLLAMA_BLAS=ON -DGGML_HIP=ON -DAMDGPU_TARGETS=gfx1101" venv/bin/pip install llama_cpp_python --no-cache-dir
