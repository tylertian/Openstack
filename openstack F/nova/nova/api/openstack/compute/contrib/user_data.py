# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack LLC.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License

from nova.api.openstack import extensions


class User_data(extensions.ExtensionDescriptor):
    """Add user_data to the Create Server v1.1 API"""

    name = "UserData"
    alias = "os-user-data"
    namespace = ("http://docs.openstack.org/compute/ext/"
                 "userdata/api/v1.1")
    updated = "2012-08-07T00:00:00+00:00"
