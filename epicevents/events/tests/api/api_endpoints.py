API_ENDPOINTS = [
    {
        'path': '/clients/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
                {
                    'name': 'post',
                    'permissions': ('sales', ),
                },
            ],
    },
    {
        'path': '/clients/me/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
            ],
    },
    {
        'path': '/clients/1/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('sales_user', ),
                },
                {
                    'name': 'put',
                    'permissions': ('sales_user', ),
                },
                {
                    'name': 'delete',
                    'permissions': ('sales_user', ),
                },
            ],
    },
    {
        'path': '/clients/1/contracts/',
        'methods':
            [
                {
                    'name': 'post',
                    'permissions': ('sales_user', ),
                },
                {
                    'name': 'get',
                    'permissions': ('sales_user', ),
                },
            ],
    },
    {
        'path': '/contracts/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
            ],
    },
    {
        'path': '/contracts/me/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
            ],
    },
    {
        'path': '/contracts/1/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('sales_user', ),
                },
                {
                    'name': 'put',
                    'permissions': ('sales_user', ),
                },
                {
                    'name': 'delete',
                    'permissions': ('sales_user', ),
                },
            ],
    },
    {
        'path': '/contracts/2/events/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('sales_user', ),
                },
                {
                    'name': 'post',
                    'permissions': ('sales_user', ),
                },
            ],
    },
    {
        'path': '/events/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
            ],
    },
    {
        'path': '/events/me/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
            ],
    },    
    {
        'path': '/events/1/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('support_user', ),
                },
                {
                    'name': 'put',
                    'permissions': ('support_user', ),
                },
                {
                    'name': 'delete',
                    'permissions': ('support_user', ),
                },
            ],
    },
]


for endpoint in API_ENDPOINTS:
    endpoint['path'] = '/api' + endpoint['path']