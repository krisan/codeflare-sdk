from codeflare_sdk.cluster.cluster import list_all_clusters, _app_wrapper_status
from codeflare_sdk.cluster.cluster import Cluster, ClusterConfiguration

#for now these tests assume that the cluster was already created
def test_list_clusters():
    clusters = list_all_clusters()

def test_cluster_status():
    cluster = Cluster(ClusterConfiguration(name='raycluster-autoscaler'))
    cluster.status()

def test_app_wrapper_status():
    print(_app_wrapper_status('raycluster-autoscaler'))
    
