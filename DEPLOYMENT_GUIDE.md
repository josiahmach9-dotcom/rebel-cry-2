# RebelCry Ministries - Vercel Deployment Guide

## Step 1: Prepare Your GitHub Repository

Make sure your GitHub repo has this structure:
```
RebelCry/
├── RebelCryProject/
│   ├── __init__.py
│   ├── settings.py          (use the one provided)
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py              (use the one provided)
├── pages/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── templates/               (your HTML templates)
│   ├── index.html
│   ├── apologetics.html
│   ├── about.html
│   ├── devotional.html
│   └── policy.html
├── static/                  (CSS, JavaScript, images)
│   ├── css/
│   ├── js/
│   └── images/
├── manage.py
├── requirements.txt         (use the one provided)
├── vercel.json             (use the one provided)
├── wsgi.py                 (use the one provided)
├── .gitignore              (use the one provided)
└── .env.example            (use the one provided)
```

## Step 2: Push to GitHub

```bash
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

## Step 3: Connect to Vercel

1. Go to https://vercel.com
2. Click "New Project"
3. Select your GitHub repository: `python-loop/RebelCry`
4. Choose "Django" as the framework (or it will auto-detect)
5. Click "Deploy"

## Step 4: Set Environment Variables in Vercel

After importing the project:

1. Go to **Project Settings** → **Environment Variables**
2. Add the following:

```
SECRET_KEY = your-secure-secret-key
DEBUG = false
ALLOWED_HOSTS = yourdomain.vercel.app,www.yourdomain.com
DATABASE_URL = (optional - if using external database)
```

### Generate a SECRET_KEY:

Run this in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use an online generator: https://djecrety.ir/

## Step 5: Database Options

### Option A: SQLite (Simple, limited)
- Works out of the box
- Limited to 1 connection
- Data resets on redeployment
- Good for prototyping only

### Option B: PostgreSQL (Recommended)
1. Add PostgreSQL database:
   - Use Vercel's PostgreSQL offering, or
   - Use a service like Neon.tech, Railway, or AWS RDS

2. Copy the connection URL to `DATABASE_URL` environment variable

## Step 6: Static Files & Media

- Static files are automatically collected during build
- For media uploads, consider using:
  - AWS S3
  - Cloudinary
  - Vercel Blob Storage (new)

Update `settings.py` to use your storage service.

## Step 7: Deploy!

1. In Vercel dashboard, go to **Deployments**
2. Click **Deploy** on the latest commit
3. Monitor the build logs
4. Once deployed, visit your site at `yourdomain.vercel.app`

## Troubleshooting

### Build Fails
- Check build logs in Vercel dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify environment variables are set

### Static Files Not Loading
- Run: `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` in settings

### Database Issues
- Ensure `DATABASE_URL` is correct
- Run migrations: `python manage.py migrate`

### Images/Media Not Showing
- Use Cloudinary or S3 for media storage
- Update Django to use the storage backend

## Custom Domain

1. In Vercel, go to **Project Settings** → **Domains**
2. Add your custom domain
3. Follow DNS setup instructions
4. Update `ALLOWED_HOSTS` in environment variables

## Security Checklist

- [ ] Set `DEBUG = false` in production
- [ ] Generate strong `SECRET_KEY`
- [ ] Set `ALLOWED_HOSTS` to your domain
- [ ] Enable HTTPS (automatic with Vercel)
- [ ] Use environment variables for sensitive data
- [ ] Regular backups if using external database

## Need Help?

- Django Docs: https://docs.djangoproject.com/
- Vercel Docs: https://vercel.com/docs
- Django + Vercel Guide: https://vercel.com/guides/django
