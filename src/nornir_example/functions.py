from nornir.core.task import Task, Result
from nornir_utils.plugins.tasks.files import write_file
from nornir_jinja2.plugins.tasks import template_file


def render_config(task: Task, template_dir: str) -> Result:
    """
    Create config from template and put it in `config` host object attribute
    """

    r = task.run(
        name="Render config",
        task=template_file,
        template="config.j2",
        path=f"{template_dir}",
    )
    task.host["config"] = r.result


def write_config(task: Task, output_dir: str) -> Result:
    """
    Save generated configs to text files
    """

    task.run(
        name="Save configs",
        task=write_file,
        filename=f"{output_dir}/{task.host}-config.txt",
        content=task.host["config"],
    )
