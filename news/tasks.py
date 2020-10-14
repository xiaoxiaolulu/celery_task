from celery_task.settings import app
from news.models import NewsCategory, News
from celery import task, platforms

platforms.C_FORCE_ROOT = True

# python3 manage.py celery worker -l INFO


@app.task
def data_new(df):
    df['category_id'] = df.apply(lambda x: sr_new(x['category']), axis=1)
    print(df)
    print(df.columns)
    from sqlalchemy import create_engine
    df = df[['title', 'url', 'ctime', 'category_id']]
    df = df.rename(columns={'ctime': 'new_time'})
    # conn = create_engine('mysql+pymysql://root:123456.a@127.0.0.1:3306/celerytask?charset=utf8', )
    # df.to_sql('news_new', conn, index=False, if_exists='append')
    for idx, row in df.iterrows():
        title = row['title']
        url = row['url']
        new_time = row['new_time']
        category_id = row['category_id']
        category_id = str(category_id)
        if category_id != 'nan':
            category_id = int(float(category_id))
            cate = NewsCategory.objects.get(id=category_id)
            new = News(title=title, url=url, new_time=new_time, category_id=cate)
            new.save()
        else:
            new = News(title=title, url=url, new_time=new_time)
            new.save()
    return 'success'


def sr_new(sr):
    new_category = NewsCategory.objects.filter(name=sr).first()
    category_id = new_category.id if new_category else None
    return category_id
