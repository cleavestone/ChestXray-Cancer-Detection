from src.cnnClassifier.pipeline.stage1_data_ingestion import DataIngestionPipeline
from src.cnnClassifier.pipeline.stage2 import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.training_pipeline import ModelTrainingPipeline
from src.cnnClassifier.pipeline.evaluation_pipeline import ModelEvaluationPipeline

if __name__ == "__main__":
    try:
        # Stage 1: Data Ingestion
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()

        # Stage 2: Prepare Base Model
        prepare_base_model_pipeline = PrepareBaseModelPipeline()
        prepare_base_model_pipeline.main()

        # Stage 3: Model Training
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()

        # Stage 4: Model Evaluation
        data_evaluation_pipeline=ModelEvaluationPipeline()
        data_evaluation_pipeline.main()

    except Exception as e:
        raise e