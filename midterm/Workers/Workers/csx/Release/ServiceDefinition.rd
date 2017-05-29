<?xml version="1.0" encoding="utf-8"?>
<serviceModel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="Workers" generation="1" functional="0" release="0" Id="8bc554b3-1c17-482d-ac25-d3d27ebfc9b7" dslVersion="1.2.0.0" xmlns="http://schemas.microsoft.com/dsltools/RDSM">
  <groups>
    <group name="WorkersGroup" generation="1" functional="0" release="0">
      <settings>
        <aCS name="Worker0:Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" defaultValue="">
          <maps>
            <mapMoniker name="/Workers/WorkersGroup/MapWorker0:Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" />
          </maps>
        </aCS>
        <aCS name="Worker0Instances" defaultValue="[1,1,1]">
          <maps>
            <mapMoniker name="/Workers/WorkersGroup/MapWorker0Instances" />
          </maps>
        </aCS>
        <aCS name="Worker1:Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" defaultValue="">
          <maps>
            <mapMoniker name="/Workers/WorkersGroup/MapWorker1:Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" />
          </maps>
        </aCS>
        <aCS name="Worker1Instances" defaultValue="[1,1,1]">
          <maps>
            <mapMoniker name="/Workers/WorkersGroup/MapWorker1Instances" />
          </maps>
        </aCS>
      </settings>
      <maps>
        <map name="MapWorker0:Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" kind="Identity">
          <setting>
            <aCSMoniker name="/Workers/WorkersGroup/Worker0/Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" />
          </setting>
        </map>
        <map name="MapWorker0Instances" kind="Identity">
          <setting>
            <sCSPolicyIDMoniker name="/Workers/WorkersGroup/Worker0Instances" />
          </setting>
        </map>
        <map name="MapWorker1:Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" kind="Identity">
          <setting>
            <aCSMoniker name="/Workers/WorkersGroup/Worker1/Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" />
          </setting>
        </map>
        <map name="MapWorker1Instances" kind="Identity">
          <setting>
            <sCSPolicyIDMoniker name="/Workers/WorkersGroup/Worker1Instances" />
          </setting>
        </map>
      </maps>
      <components>
        <groupHascomponents>
          <role name="Worker0" generation="1" functional="0" release="0" software="C:\Users\Bobur\Desktop\azure\midterm\Workers\Workers\csx\Release\roles\Worker0" entryPoint="base\x64\WaHostBootstrapper.exe" parameters="base\x64\WaWorkerHost.exe " memIndex="-1" hostingEnvironment="consoleroleadmin" hostingEnvironmentVersion="2">
            <settings>
              <aCS name="Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" defaultValue="" />
              <aCS name="__ModelData" defaultValue="&lt;m role=&quot;Worker0&quot; xmlns=&quot;urn:azure:m:v1&quot;&gt;&lt;r name=&quot;Worker0&quot; /&gt;&lt;r name=&quot;Worker1&quot; /&gt;&lt;/m&gt;" />
            </settings>
            <resourcereferences>
              <resourceReference name="DiagnosticStore" defaultAmount="[4096,4096,4096]" defaultSticky="true" kind="Directory" />
              <resourceReference name="EventStore" defaultAmount="[1000,1000,1000]" defaultSticky="false" kind="LogStore" />
            </resourcereferences>
          </role>
          <sCSPolicy>
            <sCSPolicyIDMoniker name="/Workers/WorkersGroup/Worker0Instances" />
            <sCSPolicyUpdateDomainMoniker name="/Workers/WorkersGroup/Worker0UpgradeDomains" />
            <sCSPolicyFaultDomainMoniker name="/Workers/WorkersGroup/Worker0FaultDomains" />
          </sCSPolicy>
        </groupHascomponents>
        <groupHascomponents>
          <role name="Worker1" generation="1" functional="0" release="0" software="C:\Users\Bobur\Desktop\azure\midterm\Workers\Workers\csx\Release\roles\Worker1" entryPoint="base\x64\WaHostBootstrapper.exe" parameters="base\x64\WaWorkerHost.exe " memIndex="-1" hostingEnvironment="consoleroleadmin" hostingEnvironmentVersion="2">
            <settings>
              <aCS name="Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" defaultValue="" />
              <aCS name="__ModelData" defaultValue="&lt;m role=&quot;Worker1&quot; xmlns=&quot;urn:azure:m:v1&quot;&gt;&lt;r name=&quot;Worker0&quot; /&gt;&lt;r name=&quot;Worker1&quot; /&gt;&lt;/m&gt;" />
            </settings>
            <resourcereferences>
              <resourceReference name="DiagnosticStore" defaultAmount="[4096,4096,4096]" defaultSticky="true" kind="Directory" />
              <resourceReference name="EventStore" defaultAmount="[1000,1000,1000]" defaultSticky="false" kind="LogStore" />
            </resourcereferences>
          </role>
          <sCSPolicy>
            <sCSPolicyIDMoniker name="/Workers/WorkersGroup/Worker1Instances" />
            <sCSPolicyUpdateDomainMoniker name="/Workers/WorkersGroup/Worker1UpgradeDomains" />
            <sCSPolicyFaultDomainMoniker name="/Workers/WorkersGroup/Worker1FaultDomains" />
          </sCSPolicy>
        </groupHascomponents>
      </components>
      <sCSPolicy>
        <sCSPolicyUpdateDomain name="Worker0UpgradeDomains" defaultPolicy="[5,5,5]" />
        <sCSPolicyUpdateDomain name="Worker1UpgradeDomains" defaultPolicy="[5,5,5]" />
        <sCSPolicyFaultDomain name="Worker0FaultDomains" defaultPolicy="[2,2,2]" />
        <sCSPolicyFaultDomain name="Worker1FaultDomains" defaultPolicy="[2,2,2]" />
        <sCSPolicyID name="Worker0Instances" defaultPolicy="[1,1,1]" />
        <sCSPolicyID name="Worker1Instances" defaultPolicy="[1,1,1]" />
      </sCSPolicy>
    </group>
  </groups>
</serviceModel>