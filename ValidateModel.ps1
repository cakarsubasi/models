#$PIPELINE_CONFIG_PATH="C:/Users/explo/Documents/Repositories/models/models/checkpoint/ssd_resnet50_retinanet_muscima_7.config"
#$PIPELINE_CONFIG_PATH="C:/Users/explo/Documents/Repositories/models/configurations/ssd_resnet152_v1_fpn_1024x1024_2.config"
$MODEL_DIR="C:/Users/explo/Documents/Repositories/models/models/model-new"
$TRANSCRIPT_PATH="C:/Users/explo/Documents/Repositories/models/models/model-new/transcripts/efficientdet_d1_validate.txt"
$PIPELINE_CONFIG_PATH="C:/Users/explo/Documents/Repositories/models/configurations/ssd_efficientdet_d1_640x640_coco17_tpu-8_2.config"

Start-Transcript -path ${TRANSCRIPT_PATH} -append
python research/object_detection/model_main_tf2.py `
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} `
    --model_dir=${MODEL_DIR} `
    --checkpoint_dir=${MODEL_DIR} `
    --sample_1_of_n_eval_examples=1 `
    --alsologtostderr
Stop-Transcript