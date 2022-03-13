python prepare_muscima_full_page_annotations.py

python dataset_splitter.py --source_directory=data/muscima_pp/v2.0/data/images --destination_directory=data/training_validation_test

python create_muscima_tf_record.py --data_dir=data/training_validation_test --set=training --annotations_dir=Full_Page_Annotations --output_path=data/all_classes_writer_independent_split/training.record --label_map_path=mapping_all_classes.txt
python create_muscima_tf_record.py --data_dir=data/training_validation_test --set=validation --annotations_dir=Full_Page_Annotations --output_path=data/all_classes_writer_independent_split/validation.record --label_map_path=mapping_all_classes.txt
python create_muscima_tf_record.py --data_dir=data/training_validation_test --set=test --annotations_dir=Full_Page_Annotations --output_path=data/all_classes_writer_independent_split/test.record --label_map_path=mapping_all_classes.txt

Copy-Item mapping_all_classes.txt ..

Move-Item ./data/all_classes_writer_independent_split/validation.record ../data/muscima/validation.record -Force
Move-Item ./data/all_classes_writer_independent_split/training.record ../data/muscima/training.record -Force
Move-Item ./data/all_classes_writer_independent_split/test.record ../data/muscima/test.record -Force