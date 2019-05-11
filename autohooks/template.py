# Copyright (C) 2019 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from string import Template

from autohooks.setting import Mode
from autohooks.utils import get_autohooks_directory_path


PYTHON3_SHEBANG = '/usr/bin/env python3'
PIPENV_SHEBANG = '/usr/bin/env pipenv run python'


def get_pre_commit_hook_template_path():
    setup_dir_path = get_autohooks_directory_path()
    return setup_dir_path / 'precommit' / 'template'


class PreCommitTemplate:
    def __init__(self, template_path=None):
        if template_path is None:
            template_path = get_pre_commit_hook_template_path()
        self._load(template_path)

    def _load(self, template_path):
        self._template = Template(template_path.read_text())

    def render(self, *, mode):
        mode = mode.get_effective_mode()

        if mode == Mode.PIPENV:
            params = dict(SHEBANG=PIPENV_SHEBANG)
        else:
            params = dict(SHEBANG=PYTHON3_SHEBANG)

        return self._template.safe_substitute(params)
