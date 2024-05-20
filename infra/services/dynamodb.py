from aws_cdk import aws_dynamodb as dynamodb
from lambda_forge.trackers import invoke


class DynamoDB:
    def __init__(self, scope, resources: dict) -> None:
        self.tables = {
            # "table_id": dynamodb.Table.from_table_arn(scope, "Dynamo", resources["arns"]["dynamo_arn"])
        }
        
    @invoke(service="dynamodb", resource_id="table_id", function="function")
    def grant_write_data(self, table_id, function):
        table = self.tables.get(table_id)
        table.grant_write_data(function)
