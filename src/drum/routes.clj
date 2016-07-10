(ns drum.routes
  (:require [compojure.route :as route]
            [compojure.core :refer [GET PUT POST DELETE defroutes context]]))



(defroutes app-routes
           (GET "/" [] "Hello World")
)