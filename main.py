import pandas as pd
from eurekaai.components.pipelines import pipeline
from eurekaai.components.steps import step, Output
from eurekaai.config.container import ContainerSetting
from eurekaai.config.kubeflow import KubeflowSettings
from eurekaai.config.resource import ResourceSettings
import eurekaai.config.client as client

NAMESPACE = "atul-bharadwaj-1"
USERNAME = "atul.bharadwaj@symphonyai.com"  # This is the username for the profile you want to use
PASSWORD = "MTcxNTA3NTc5MnxOd3dBTkVKVE1qWlBNMVV5VUV0V1ZrZFpSMUpTVlVoWlVGVlhNalJSU0VKQ1FVTkxUbFphVDFGT1VraFhXVTFKVVV0SVIxVk1XRUU9fHQfucgOexYtGnlX0KKmiXyS5HjCnX8XkIuo83i2v6il"

kubeflow_setting = KubeflowSettings(username=USERNAME, key=PASSWORD, namespace=NAMESPACE, synchronous=True)

container_settings = ContainerSetting(parent_image="crescendoimages.azurecr.io/eureka_dml_pipeline:v4.7.0.2",
                                      requirements=["kfp ==1.8.16", "pyarrow",
                                                    "typing_extensions==4.7.1",
                                                    "pydantic==1.10.12", "pyiceberg==0.4.0"])


@step()
def load_dataset_via_dl() -> None:
    print("-------hello world------")


@pipeline(enable_cache=False,settings={"container": container_settings, "kubeflow": kubeflow_setting})
def data_library_pipeline(load_dataset_via_dl):
    load_dataset_via_dl()


if __name__ == "__main__":
    pipeline_instance = data_library_pipeline(
        load_dataset_via_dl=load_dataset_via_dl()
    )
    pipeline_instance.run(unlisted=True)