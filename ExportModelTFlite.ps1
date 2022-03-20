
$PIPELINE_CONFIG_PATH="configurations\ssd_resnet152_v1_fpn_1024x1024_1.config"
$TRAINED_CKPT_PREFIX="models/model-new/"
$EXPORT_DIR="export/tflite"
python research/object_detection/export_tflite_graph_tf2.py `
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} `
    --trained_checkpoint_dir=${TRAINED_CKPT_PREFIX} `
    --output_directory ${EXPORT_DIR}