from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier.components.evaluate import Evaluation
from cnnClassifier import logger

STAGE_NAME="Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        eval_config=config.get_evaluation_config()
        evaluation=Evaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_evaluation_pipeline=ModelEvaluationPipeline()
        data_evaluation_pipeline.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


