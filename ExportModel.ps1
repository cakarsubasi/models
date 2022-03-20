$INPUT_TYPE="image_tensor"
$PIPELINE_CONFIG_PATH="configurations/ssd_resnet152_v1_fpn_1024x1024_2.config"
$TRAINED_CKPT_PREFIX="models/model-new/"
$EXPORT_DIR="export"
python research/object_detection/exporter_main_v2.py `
    --input_type=${INPUT_TYPE} `
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} `
    --trained_checkpoint_dir=${TRAINED_CKPT_PREFIX} `
    --output_directory=${EXPORT_DIR}