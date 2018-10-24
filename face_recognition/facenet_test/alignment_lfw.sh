for N in {1..4}; do \
    python src/align/align_dataset_mtcnn.py \
    /home/lc/lcl/jlq_action/datasets/lfw/raw \
    /home/lc/lcl/jlq_action/datasets/lfw/lfw_mtcnnpy_160 \
    --image_size 160 \
    --margin 32 \
    --random_order \
    & done

