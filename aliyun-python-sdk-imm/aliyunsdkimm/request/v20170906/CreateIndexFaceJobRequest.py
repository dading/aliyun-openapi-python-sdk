# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateIndexFaceJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'CreateIndexFaceJob','imm')

	def get_Chain(self):
		return self.get_query_params().get('Chain')

	def set_Chain(self,Chain):
		self.add_query_param('Chain',Chain)

	def get_SrcUris(self):
		return self.get_query_params().get('SrcUris')

	def set_SrcUris(self,SrcUris):
		self.add_query_param('SrcUris',SrcUris)

	def get_NotifyTopicName(self):
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self,NotifyTopicName):
		self.add_query_param('NotifyTopicName',NotifyTopicName)

	def get_NotifyEndpoint(self):
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self,NotifyEndpoint):
		self.add_query_param('NotifyEndpoint',NotifyEndpoint)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_SetId(self):
		return self.get_query_params().get('SetId')

	def set_SetId(self,SetId):
		self.add_query_param('SetId',SetId)

	def get_Force(self):
		return self.get_query_params().get('Force')

	def set_Force(self,Force):
		self.add_query_param('Force',Force)