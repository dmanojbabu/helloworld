from pybuilder.core import init,use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.pylint")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

#default_task = "publish"
default_task = ['install_dependencies', 'clean', 'analyze', 'publish']

VIOLATION_PYLINT_OPTIONS = ["--output-format=parseable"]

@init
def initialize(project):
    project.build_depends_on('mockito')
    project.set_property("pylint_options", VIOLATION_PYLINT_OPTIONS)

