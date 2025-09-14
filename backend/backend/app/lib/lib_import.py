import os, enum, re, uuid

from enum import Enum
from uuid import uuid4

# typing
from typing import List, Optional, Annotated

# pydantic
from pydantic import (
    BaseModel, EmailStr, StringConstraints, field_validator
)

# fastapi
from fastapi import (
    APIRouter, FastAPI, Depends, HTTPException, Query,
    status, UploadFile, File
)
from fastapi.middleware.cors import CORSMiddleware

# passlib
from passlib.hash import bcrypt

# dotenv
from dotenv import load_dotenv

# sqlalchemy
from sqlalchemy.orm import Session, relationship, validates, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, BigInteger, SmallInteger, Float, Boolean,
    String, Enum, DateTime, ForeignKey, UniqueConstraint, CheckConstraint,
    Time, Text, create_engine
)

# Remove Base import to avoid circular import issues
# Base = declarative_base()

# datetime
from datetime import datetime, timezone, time, timedelta
