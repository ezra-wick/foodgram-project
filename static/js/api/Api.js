class Api {
  constructor(apiUrl) {
    this.apiUrl = apiUrl;
  }

  async getPurchases() {
    const e = await fetch(`$(this.apiUrl)/api/v1/purchases/`, {
      headers: {
        'Content-Type': 'application/json',
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async addPurchases(id) {
    const e = await fetch(`/api/v1/purchases/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      body: JSON.stringify({
        id: id
      })
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async removePurchases(id) {
    const e = await fetch(`/api/v1/purchases/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async addSubscriptions(id) {
    const e = await fetch(`/api/v1/subscriptions/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      body: JSON.stringify({
        id: id,
      })
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async removeSubscriptions(id) {
    const e = await fetch(`/api/v1/subscriptions/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async addFavorites(id) {
    const e = await fetch(`/api/v1/favorites/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      body: JSON.stringify({
        id: id
      })
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }

  async removeFavorites(id) {
    const e = await fetch(`/api/v1/favorites/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }
  
  async getIngredients(text) {
    const e = await fetch(`/api/v1/ingredients?query=${text}`, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    if (e.ok) {
      return e.json();
    }
    return await Promise.reject(e.statusText);
  }
}
