from datetime import datetime
from ..expression_evaluator import ExpressionEvaluator, EvaluateExpressionDelegate
from ..expression_type import UTCNOW
from ..function_utils import FunctionUtils
from ..return_type import ReturnType

class UtcNow(ExpressionEvaluator):
    def __init__(self):
        super().__init__(
            UTCNOW, UtcNow.evaluator(), ReturnType.String, UtcNow.validator
        )

    @staticmethod
    def evaluator() -> EvaluateExpressionDelegate:
        def anonymous_function(args: list):
            date_time = datetime.utcnow()
            if len(args) == 1:
                return date_time.strftime(args[0])
            return date_time.strftime(FunctionUtils.default_date_time_format)[:-4] + "Z"
        return FunctionUtils.apply(anonymous_function)

    @staticmethod
    def validator(expression: object):
        FunctionUtils.validate_order(expression, [ReturnType.String])
