#$PIPELINE_CONFIG_PATH="C:/Users/explo/Documents/Repositories/models/models/checkpoint/ssd_resnet50_retinanet_muscima_7.config"
$PIPELINE_CONFIG_PATH="C:/Users/explo/Documents/Repositories/models/models/checkpoint/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.config"
$MODEL_DIR="C:/Users/explo/Documents/Repositories/models/models/model-new"
python research/object_detection/model_main_tf2.py --pipeline_config_path=${PIPELINE_CONFIG_PATH} --model_dir=${MODEL_DIR} --alsologtostderr