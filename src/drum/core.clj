(ns drum.core
  (:gen-class)
  (:require [aleph.http :as http]
            [drum.routes :refer :all]
            [ring.middleware.json :as middleware]
            [ring.middleware.defaults :refer [wrap-defaults api-defaults]]))

(def app
  "Define ring middleware settings using compojure routes"
  (-> app-routes
      (wrap-defaults api-defaults)
      (middleware/wrap-json-body)
      (middleware/wrap-json-response)))

(defn -main
  "Run the HTTP Server on specific port using defined ring middleware settings"
  []
  (let [port 3000]
    (http/start-server app {:port port})
    (println "Http Server has started on port:" port)))
