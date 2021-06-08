"""
Add symbols that can be used as project level constants.
Makes for easy refactoring in case of renames, typos and keeping values consistent.
"""
import os

N_DEFAULT_CORES = 8
N_MIN_CORES = 1
N_EVAL_BATCH_SIZE = 8
N_EVAL_SPLIT = 0.1
N_EPOCHS = 10
k = 1000

NAME = "name"
MODEL_NAME = "model_name"
CORES = "cores"
DATA_ID = "data_id"
DATA = "data"
TAG = "detailed_tags"
ALTERNATIVES = "alternatives"
DATASETS = "datasets"
MODELS = "models"
METRICS = "metrics"
INTENT = "intent"
INTENTS = "intents"
ENTITIES = "entities"
SENTENCE_ID = "sentence_id"
WORDS = "words"
LABELS = "labels"
REPORT = "report"
VERSION = "version"
TRAIN = "train"
TEST = "test"
DEFAULT = "default"
DEV = "dev"
PROD = "prod"
EPOCHS = "epochs"
CLASSIFICATION = "classification"
NER = "ner"
TASKS = "tasks"
ALIAS = "alias"
THRESHOLD = "threshold"
RULES = "rules"
SLOTS = "slots"
TOOL = "tool"
POETRY = "poetry"
MASTER = "master"
CONTEXT = "context"
TRANSCRIPT = "transcript"
TEXT = "text"
CONFIDENCE = "confidence"
INIT = "init"
CLONE = "clone"
REPL = "repl"
RELEASE = "release"
CSV = "csv"
SQLITE = "sqlite"
USE = "use"
FORMAT = "format"
ENVIRONMENT = "environment"
PRODUCTION = "production"
TRUE_LABEL = "true_label"
PRED_LABEL = "pred_label"
VALUE = "value"
VALUES = "values"
POSTPROCESS = "postprocess"
PLUGIN = "plugin"
PARAMS = "params"
RULE_BASED_PLUGIN = "RuleBasedSlotFillerPlugin"



S_TRAIN_DATA = "train.csv"
S_TEST_DATA = "test.csv"
S_CONFIG_PATH = os.path.join("config", "config.yaml")
S_INTENT_LABEL_ENCODER = "labelencoder.pkl"
S_ENTITY_LABELS = "entity_label_list.pkl"
S_XLMR = "xlmroberta"
S_XLMRB = "xlm-roberta-base"
S_REPORT = "report.csv"
S_CLASSIFICATION_TASK = "intent_classification"
S_EXTRACTION_TASK = "entity_extraction"
S_BEST_MODEL = "best_model_dir"
S_OUTPUT_DIR = "output_dir"
S_EVAL_DURING_TRAINING_STEPS = "evaluate_during_training_steps"
S_EVAL_BATCH_SIZE = "eval_batch_size"
S_MODEL_ARGS = "model_args"
S_NUM_TRAIN_EPOCHS = "num_train_epochs"
S_PROJECT_TOML = "pyproject.toml"
S_CHANGELOG = "CHANGELOG.md"

S_INTENT_ERROR = "_error_"
S_INTENT_OOS = "_oos_"
S_CLASSIFICATION_INPUT = "classification_input"
S_NER_INPUT = "ner_input"
S_CONTEXT = "context"
S_ERRORS = "errors.csv"
S_INTENTS_INFO = "intents_info"
S_REFERENCE_TIME = "reference_time"
S_LOCALE = "locale"

V_SUPPORTED_DATA_FORMATS = [CSV, SQLITE]
LANG_TO_LOCALES = {
    "en": "en_IN", # This should be set via config
    "hi": "hi_IN"
}

CLIENTS_CONFIGS_ROUTE = "/clients/configs/"
REQUEST_MAX_RETRIES = 5