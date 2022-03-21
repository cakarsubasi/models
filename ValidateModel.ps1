#$PIPELINE_CONFIG_PATH="C:/Users/explo/Documents/Repositories/models/models/checkpoint/ssd_resnet50_retinanet_muscima_7.config"
$PIPELINE_CONFIG_PATH="C:/Users/explo/Documents/Repositories/models/configurations/ssd_resnet152_v1_fpn_1024x1024_2.config"
$MODEL_DIR="C:/Users/explo/Documents/Repositories/models/models/model-new"

Start-Transcript -path "C:/Users/explo/Documents/Repositories/models/models/model-new/transcripts/resnet152.txt" -append
python research/object_detection/model_main_tf2.py `
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} `
    --model_dir=${MODEL_DIR} `
    --checkpoint_dir=${MODEL_DIR} `
    --num_workers=4 `
    --sample_1_of_n_eval_examples=1 `
    --alsologtostderr
Stop-Transcript