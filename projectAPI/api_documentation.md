# Updated based on feedback
# Module 4 Project — Part 2: API Documentation

**Name:** Nicco Gonzalez
**Date:** 06-28-2026

---

# Introduction

This document summarizes the three public APIs explored in `api_explorer.py`. For each API, it includes the base URL, authentication requirements, endpoints tested, sample requests and responses, any observed rate limits, and noteworthy behaviors encountered during testing.

---

# API 1: JSONPlaceholder

## Overview

JSONPlaceholder is a free fake REST API used for testing and learning HTTP requests. It allows developers to practice GET, POST, PUT, PATCH, and DELETE requests without modifying real data.

### Base URL

```
https://jsonplaceholder.typicode.com
```

### Authentication

No authentication is required.

### Endpoints Tested

---

### 1. GET /users

**Request**

```http
GET https://jsonplaceholder.typicode.com/users
```

**Purpose**

Retrieves a list of all users.

**Sample Response**

```json
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz"
  }
]
```

---

### 2. GET /posts?userId=1

**Request**

```http
GET https://jsonplaceholder.typicode.com/posts?userId=1
```

**Purpose**

Retrieves all posts created by User 1.

**Sample Response**

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati",
    "body": "quia et suscipit..."
  }
]
```

---

### 3. POST /posts

**Request**

```http
POST https://jsonplaceholder.typicode.com/posts
```

**Request Body**

```json
{
  "title": "Learning REST APIs",
  "body": "Testing POST request",
  "userId": 1
}
```

**Sample Response**

```json
{
  "title": "Learning REST APIs",
  "body": "Testing POST request",
  "userId": 1,
  "id": 101
}
```

**Purpose**

Creates a simulated post and returns the created object.

### Rate Limits

No rate limits were encountered during testing.

### Surprise / Unexpected Behavior

Although the POST request returns a newly created object with an ID, the data is not permanently saved. JSONPlaceholder simulates successful POST requests without modifying any actual database.

---

# API 2: PokeAPI

## Overview

PokeAPI is a free REST API that provides detailed information about Pokémon, abilities, moves, types, species, and many other game resources.

### Base URL

```
https://pokeapi.co/api/v2
```

### Authentication

No authentication is required.

### Endpoints Tested

---

### 1. GET /pokemon/25

**Request**

```http
GET https://pokeapi.co/api/v2/pokemon/25
```

**Purpose**

Retrieves information about Pikachu.

**Sample Response**

```json
{
  "id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "abilities": [
    {
      "ability": {
        "name": "static"
      }
    }
  ]
}
```

---

### 2. Follow Pokémon Type URL

After retrieving Pikachu, the script follows the URL contained in the response:

```
https://pokeapi.co/api/v2/type/13/
```

**Purpose**

Retrieves all Pokémon that share Pikachu's Electric type.

**Sample Response (Partial)**

```json
{
  "pokemon": [
    {
      "pokemon": {
        "name": "pikachu"
      }
    },
    {
      "pokemon": {
        "name": "raichu"
      }
    }
  ]
}
```

### Rate Limits

No rate limits were encountered during testing.

### Surprise / Unexpected Behavior

One interesting feature of PokeAPI is that many responses contain URLs pointing to related resources instead of embedding all information in a single response. This allows applications to follow links to retrieve additional data only when needed.

---

# API 3: REST Countries

## Overview

REST Countries provides country information including names, capitals, regions, populations, currencies, languages, flags, and more.

### Base URL

```
https://restcountries.com/v3.1
```

### Authentication

No authentication is required.

### Endpoints Tested

---

### 1. GET /name/japan

**Request**

```http
GET https://restcountries.com/v3.1/name/japan
```

**Purpose**

Retrieves information about Japan.

**Sample Response**

```json
[
  {
    "name": {
      "official": "Japan"
    },
    "capital": [
      "Tokyo"
    ],
    "population": 123294513,
    "region": "Asia"
  }
]
```

---

### 2. GET /region/asia

**Request**

```http
GET https://restcountries.com/v3.1/region/asia
```

**Purpose**

Returns all countries located in Asia.

**Sample Response (Partial)**

```json
[
  {
    "name": {
      "common": "Japan"
    }
  },
  {
    "name": {
      "common": "China"
    }
  }
]
```

---

### 3. GET /name/thiscountrydoesnotexist

**Request**

```http
GET https://restcountries.com/v3.1/name/thiscountrydoesnotexist
```

**Purpose**

Tests how the API handles requests for nonexistent resources.

**Response**

```
404 Not Found
```

The script checks the status code and prints a friendly message instead of crashing.

### Rate Limits

No rate limits were encountered during testing.

### Surprise / Unexpected Behavior

Instead of returning an empty list when a country is not found, REST Countries returns a 404 Not Found response. This required checking the response status before attempting to process the JSON data.

---

# Overall Observations

* All three APIs use REST principles and return JSON responses.
* None of the APIs required authentication for the endpoints tested.
* The APIs were straightforward to consume using Python's `requests` library.
* JSONPlaceholder is useful for practicing CRUD operations without affecting real data.
* PokeAPI demonstrates a linked-resource design by including URLs to related resources in many responses.
* REST Countries provides comprehensive geographic data while using standard HTTP status codes for error handling.

Overall, these APIs provided valuable experience making GET and POST requests, handling successful and unsuccessful responses, parsing JSON, and understanding how different REST APIs organize and expose their resources.
